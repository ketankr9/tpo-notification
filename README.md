# tpo-notification
A script which checks tpo portal every x seconds for any new company added to company visit and sends you a SMS notification<br/>
pip install dryscrape bs4 ; if pip failed try clonning respective library and manually installing (python setup.py install)<br/><br/>
A way2sms free account is needed for SMS service. Please be carefull as..the email entered while signup may receive occassional spam mails. Only valid phone number is needed to receive sms, you may enter anything@gmail.com as email. <br/>
<br/>The implementation of way2sms script is beautiful, it uses cookies to authenticate login expplicitly and passes it between sessions.<br/><br/>
<strong>One speciality of the way2sms script is that it fills the remaining message ( if len(message)<140 ) with <i>spaces</i>  which lefts no space for extra line appended by the way2sms("This sms is sent via way2sms link etc") by javascript while using its site on browser.</strong> Not clear? try sending a message via its site on browser and by this script and see the difference.<br/><br/>
A similar implementation is needed for logging into placement.iitbhu.ac.in, as of now dryscrape is used (which is unnecessary).<br/><br/>

Liked the implementation ? Fork it and try your own implementation : Raise an issue.


