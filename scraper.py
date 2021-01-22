import bs4, requests, smtplib
print ("Imported")

# ------------------- E-mail list ------------------------
toAddress = ['handerson5486@gmail.com']
             #'wcgoodridge@gmail.com','claudia.goodridge@gmail.com']
# --------------------------------------------------------

# Download page
getPage = requests.get('https://www.ruhealth.org/covid-19-vaccine')
getPage.raise_for_status() #if error it will stop the program

# Parse text for foods
rawHTML = bs4.BeautifulSoup(getPage.text, 'html.parser')
#print(rawHTML.prettify())
# Count number of "Full" occurrences 
stringHTML = str(rawHTML)
counter = stringHTML.count('Full.png')
counter2 = stringHTML.count('AM -') + stringHTML.count(' am –')
print(counter)
print(counter2)


#Determine if there is an open slot
openSlot = False
if (counter/2) != counter2:
    if(counter/2) < counter2:
        openSlot = True
print(openSlot)

#Send email if open slot
if openSlot == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When password is sent, it will be encrypted.
    conn.login('handerson5486@gmail.com', 'opyxkmyebpexvzmx')
    conn.sendmail('handerson5486@gmail.com', toAddress, 'Subject: Potential Opening\n\nHi Amma and Abba\n\nThe script has detected a change, there may be an appointment available.\n\nThis is an automated message.\nVaccine Scraper V1.0')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('No change detected.')
