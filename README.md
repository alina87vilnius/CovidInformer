# CovidRateInformer
Service informs via SMS about the 14-day rate of newly reported COVID-19 cases per 100 000 population in Lithuania.

# More Info
Code is hosted on [PythonAnywhere](https://www.pythonanywhere.com/) with the scheduled task at 10:00 UTC.<br>
COVID-19 statistics are get from **API**.<br>
Rate is calculated as the difference between the total number of COVID-19 cases on a report day and a day 14 days earlier per 100 000 population.<br>
SMS is sent with the help of the [Twilio](https://www.twilio.com/) platform.

# Data Source
**[Lithuanian Department of Statistics](https://osp.stat.gov.lt/)**

- COVID-19 aggregated information [dashboard](https://open-data-ls-osp-sdg.hub.arcgis.com/datasets/d49a63c934be4f65a93b6273785a8449_0) (API)<br>
*According to documentation data is updated daily at 08:00 UTC.*

- [Database](https://osp.stat.gov.lt/statistiniu-rodikliu-analize?hash=5b7fa09d-7ace-4909-89d9-b8a8897da5ba#/) of population indicators<br>
*As the database provides indicators for the beginning of the year, provisional data for 2021 is used.*
