# nhacks-2020
nhacks 2020 project submission

## Idea
Smoke detector for vapes

## Function
Detects certain molecules/compounds released by vapes in the air and alerts staff.

## Practicality 
Deters the usage of vapes which are harmful to the human body- especially to young adults/teenagers

## Inspiration
After spending a year at Tuscarora HS, being able to smell the cotton candy vapes throughout the entire school was a problem we should not have had to get used to. With that memory driving us, we devised an idea regarding the health and safety of students in schools, and planned to significantly decrease the amount of vapes at school. 

## What it does
The Vape Deterrence Unit (VDU) functions with [nitrogen-doped graphene sheets](https://www.researchgate.net/publication/311506022_Electrochemical_sensing_of_nicotine_using_screen-printed_carbon_electrodes_modified_with_nitrogen-doped_graphene_sheets), which reacts to the nicotine concentration in the air with a very low threshold, making it a perfect way to detect small traces of nicotine in the air. After the nitrogen-doped sheets react, they drop in voltage, allowing the digital multi-meter behind the sheets to communicate with the Raspberry Pi in the server room. The Pi checks to see if the voltage drop is enough to merit a silent alarm and sends an email with the report to the proper authorities.

## What's next for temp
Now, all that remains is to truly build the device. If we were at an in-person hackathon, we'd be sure to 3D print our design, and have MLH provide us with the multi-meter as well as the Raspberry Pi. However, we're unable to do that due to the nature of the virtual hackathon. Our next steps would be to actually produce the device.
