<html>
<h1>Introduction</h1>
<body>A search-engine based database comprised of safety infromation of medications for older adults from Beers List and STOPP/START Toolkit. Provides concise guidelines for healthcare professionals to help improve the safety of prescribing medications for geriatric population. Designed and developed in cooperation with geriatric clinic at St. Joseph's Health Centre in Toronto, Ontario. </body>
</html>


# Database for Medication Safety in Geriatric (DMSG)

DMSG is web application that allows user to access safety infromation of medications for older adults from both BEERS criteira and STOPP/START Toolkit. It is intended to be use within a healthcare institution where healthcare professionals can sign-in to the application and share notes with each other regarding any medication, drug class and recommendation in the database. This repository provides the framework of the application (along with the database).

## Demo 
In the following demo, you will see an user accessing the guideline in database, posting a note under one of the medication and viewing other notes that were posted.

<img src="./misc/demo.gif"/>

## Usage

1. Click [here](https://your-twitch-clips.herokuapp.com/) to view it in the browser.
2. To view guidelines from BEERS and STOPP/START, simply click on any medication/drug classes under "Medications" or "Drug Classes" in navigation bar.
3. To view and post notes, you have to register and sign-in to an account. 
4. Click on "Submit Note" or "View Note" button under each medication/drug class to submit or read note.
5. Each user is only allowed to post 1 note per medication/drug class, posting another note will override old note.

## Getting Started
This repository siply provides the framework of the web application and some code will need to be changed to accomadate each healthcare institution. 

### Clone this project

```bash
  cd ~/projects
  git clone https://github.com/calvinhychu/YourTwitchClips.git
  cd YourTwitchClips
```
### Code that needs modificaiton
1. Change config.cfg for secret key, postgreSQL location and email server
2. Change check_email_domain under forms.py to restrain email accounts from one certain domain to be able to register for an account 


## How it works?
YourTwitchClips utilizes Twitch API to get access of Twitch user's follow list and list of top clips from each followed channel. 

YourTwitchClips uses axios to make HTTP call from client-side to server-side, server-side then make HTTP call to Twitch API and return it back to client-side.

Server-side takes advantage of Express.js module for routing and API call. 

## Guidelines
BEERS criteria and STOPP/START criteria are two most prominent guidelines for healthcare professionals to help improve the safety of prescribing medications for older adults. BEERS criteria is a guideline published by American Geriatric Society in 2015 to identify potentially inappropriate medication use in geriatric population. You can click [here](https://www.guidelinecentral.com/summaries/american-geriatrics-society-2015-updated-beers-criteria-for-potentially-inappropriate-medication-use-in-older-adults/#section-society
to view the full publication of BEERS criteria. STOPP (Screening Tool of Older Persons’ Prescriptions) and START (Screening Tool to Alert to Right Treatment) are explicit criteria that facilitate medication review in multi-morbid older people in most clinical settings. You can click [here](https://www.tandfonline.com/doi/abs/10.1080/17512433.2020.1697676?journalCode=ierj20) to view full publication of STOPP/START.

## Disclaimer
DMSG is designed and created by Calvin Chu in Aug, 2020. It is developed in cooperation with Anticoagulation clinic and Geriatric clinic at St Joseph Healthcare Center, Toronto, Ontario. However, it is not affiliated with St Joseph Healthcare Center, BEERS criteria and STOPP/START criteria. This website only intended to be used for non-profit purpose. All guidelines are properties of BEERS criteria or STOPP/START criteria.