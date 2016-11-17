# Secret Santa sending email script
# The purpose of the script to randomly select email and randomly assigned name for that email
# This script creates a dictionary with the key = email and value = name {email: name}
# The input is participant_dictionary, the output is SecretSanta_dictionary which is used to sending mail
# The scripts creates two supporting lists participant_names_list and participant_emails_list
# Each iteration the random name and email are selected and new SecretSanta_dictionary pair is added
# Selected name and email are deleted from the dictionary
# Iteration continues until all names are assigned to some email

import smtplib
import email.utils
from email.mime.text import MIMEText
import random

participant_dictionary = {'Uliana': 'Uliana.Mogylova@globalrelay.net', 'Mike': 'Mike.Donovan@globalrelay.net', 'Spencer': 'Spencer@globalrelay.net', 'Monte': 'Monte@globalrelay.net', 'Mark': 'Mark@globalrelay.net', 'Vlado': 'Vlado@globalrelay.net', 'Scott': 'Scott@globalrelay.net'}
participant_names_list = []
participant_emails_list = []
SecretSanta_dictionary = {}


# function to send mail, not tested yet, need to setup smtp server first
def sent_message(recipient, your_name):
    # Create the message
    msg = MIMEText('You are Secret Santa for '+ your_name)
    msg['To'] = email.utils.formataddr(('Recipient', recipient))
    msg['From'] = email.utils.formataddr(('Author', 'test@example.com'))
    msg['Subject'] = 'Secret Santa'

    server = smtplib.SMTP('127.0.0.1', 1025)
    server.set_debuglevel(True)  # show communication with the server
    try:
        server.sendmail('test@example.com', [recipient], msg.as_string())
    finally:
        server.quit()


# random number generation inside the range from 0 to max_range_number
def random_name(max_range_number):
    return random.randint(0, max_range_number)


# main function which creates SecretSanta_dictionary
def create_secret_santa_dictionary():
    global SecretSanta_dictionary

    # generate random name from the list participant_names_list
    name_index = random_name(len(participant_names_list)-1)
    print('name_index=', name_index)
    name = participant_names_list[name_index]
    print(name)

    # generate random email from the participant_emails_list
    email_index = random_name(len(participant_emails_list)-1)
    print('email_index=', participant_emails_list)
    email = participant_emails_list[email_index]
    print(email)

    # check that name and email are different
    if name not in email:
        # create secret santa pair {email:name}
        SecretSanta_dictionary[email] = name
        # delete name from the participant_names_list
        del participant_names_list[name_index]
        print(participant_names_list)
        # delete email from the participant_emails_list
        del participant_emails_list[email_index]
        print(participant_emails_list)


def create_global_lists():
    global participant_names_list, participant_emails_list
    # create the list of names from the global dictionary
    participant_names_list = list(participant_dictionary.keys())
    print(participant_names_list)

    # create the list of mails from the global dictionary
    participant_emails_list = list(participant_dictionary.values())
    print(participant_emails_list)

# first time create global list
create_global_lists()

while len(participant_emails_list) > 0:
    # check if the last name and the last email is the same person
    # if yes, re-create again global dictionaries
    # otherwise continue create SecretSantaDictionary
    if (len(participant_names_list) == 1) and (len(participant_emails_list) == 1) \
            and (participant_names_list[0] in participant_emails_list[0]):
        create_global_lists()
    else:
        create_secret_santa_dictionary()

if len(participant_names_list) != 0:
    # assign the last name to Uliana.Mogylova@globalrelay.net mail
    SecretSanta_dictionary = {'Uliana.Mogylova@globalrelay.net': participant_names_list[0]}

# TODO call function to send mails

print("SecretSantaDictionary=")
print(SecretSanta_dictionary)