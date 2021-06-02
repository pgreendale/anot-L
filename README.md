# anot-L
Basic notifier for available Dates in the "KFZ Meldebehörde" of "Ordnungsamt Leipzig" for a new registration of vehicles.  

## descr. 
Since pandemic times, there is no possibility of simply going to any agency at a random date and wait for open doors without an appointment. 
Despite online registration increases efficiency of the whole agency a lot, it became a nightmare to find free dates as someone who cant stay all day in front of the webbrowser and reload to wait for free appointments (mostly by people returning their former appointment). 

This basic script just clicks every five minutes through the first stages of the page and returns a high tone if appointments are available and a low tone if no appointments are available. 
This program has (and won't have in future) any further functions than notifying if appointments became available. Those clicks would be fair if you do them by yourself. 

Appointments are watched from "KFZ-Zulassungsbehörde" , not from "Zusätzliche Termine". 

## needs
* python3 
* firefox webbrowser
* webdriver from selenium library
* geckodriver to control firefox
* winsound library for notification 

## disclaimer 
Nutzung auf eigenes Risiko. Ich übernehme keine Haftung für Zuverlässigkeit und Funktion des Programms sowie jegliche aus der Nutzung des Scripts hervorgegangener Schäden und Verluste.

Falls das Script nützlich war und damit Stunden langweiligen Klickens erspart werden konnten, kannst du mir helfen und ein Bier spendieren :D 
https://www.paypal.com/paypalme/bugvitch
