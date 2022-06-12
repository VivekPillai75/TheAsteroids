This project aims to classify the data of Threshold Crossing Events (TCE) of various exoplanets using a machine learning (ML) model. Here we have used Random Forest algorithm to classify various TCE. 
The project involves a web application that takes in a CSV file as input, processes it in the ML model and outputs the predictions as a downloaded CSV file along with some graphs on HTML pages in the web browser. 

REQUIREMENTS-
A) One of the requirements is a CSV File which should include the following columns:-
1.Kepler Id (kepid)
2.TCE Planet Number (tce_plnt_num)
3.TCE Period (tce_period)
4.TCE Period Error (tce_period_err)
5.Transit Epoch (tce_time0bk)
6.Transit Epoch Error (tce_time0bk_err)
7.Impact Parameter (tce_impact)
8.Impact Parameter Error (tce_impact_err)
9.Transit Duration (tce_duration)
10.Transit Duration Error (tce_duration_err)
11.Transit Depth (tce_depth)
12.Transit Depth Error (tce_depth_err)
13.Transit Signal-to-noise Ratio (tce_model_snr)
14.Planet Radius (tce_prad)
15.Planet Radius Error (tce_prad_err)
16.Equilibrium Temperature (tce_eqt)
17.Equilibrium Temperature Error (tce_eqt_err)
18.Stellar Effective Temperature (tce_steff)
19.Stellar Effective Temperature Error (tce_steff_err)
20.Stellar Surface Gravity (tce_slogg)
21.Stellar Surface Gravity Error (tce_slogg_err)
22.Stellar Radius (tce_sradius)
23.Stellar Radius Error (tce_sradius_err)

B) The user should have the following python libraries pre-installed:-
1.Plotly
2.Flask
3.NumPy
4.Pandas
5.SKlearn

Instructions to Host The Web App on a Local Host Server:

1. Make sure the above python libraries are installed.
2. Ensure that the directory in your command prompt/terminal is changed to the directory where the folder "files" has been stored in your device. (You basically need to navigate to the folder "files" using the 'cd' command).
3. Execute the command: a) python main.py (for Windows)  
                        b) python3 main.py (for Linux)
4. After the execution of the above mentioned command, a URL comes up on the terminal, which is the address to our webpage.
5. Copy the address and paste it on your web browser and you are done!

(Caution: The process gets terminated on executing Ctrl+C. Don't press Ctrl+C more than once while copying the URL in Windows Device. You can ignore this warning in case you are working on Linux as you use Ctrl+Shift+C for copying there.)

This brings us to the end of this file. Hope you enjoy using the web application!