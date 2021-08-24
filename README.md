# Flight-Deal-Alerts
</br>
DESCRIPTION:</br>
-- This is an implementation of a flight deal alert application using python.</br>
-- It reads your desired price from a google sheet and notifies you if the flight of your choice is under that fare.</br>
-- It uses the Sheety API(https://api.sheety.co) to interact with your google sheets.</br>
-- You should have an excel sheet as shown in the screenshot with IATA code and the price below which you need alerts.</br>
-- Sheety API reads the data from google sheets and then feeds it to the application.</br>
-- Flight deals are fetched using Tequila API(https://tequila-api.kiwi.com).</br>
-- If the price is below what is mentioned in the sheet, the application triggers the twilio service and that flight deal is notified to the user.</br>
-- This can be modified so that a notification is sent to all the registered users through email(using smtplib library).</br>
</br>
APIs AND SERVICES USED:</br>
- Sheety API(https://api.sheety.co)
- Tequila API(https://tequila-api.kiwi.com)
- Twilio for messaging(https://www.twilio.com/)
