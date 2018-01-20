# Text Generation using LTSM
**Version 1.0**

Generative model for text using LSTM recurrent neural networks in Python with Keras

--- 

## Installation 

1. Install Python and Keras on your device

2. Download this repository

3. To use the complex (but slow) neural network:

      * run $python TextGenerationLTSM1.py
      
      * change the 'filename' variable (line 57) to the weight file containing the lowest lost; typically the last weight file.

        eg: filename = "weights/weights-improvement-47-1.2219-bigger.hdf5"
      
      *  Then, run $python TextGenerationLTSM2.py
      
      
   
   To use the faster (but less accurate) version:  
   
      * run $python TextGenerationSlow1.py
      
      * change the 'filename' variable (line 46) to the weight file containing the lowest lost; typically the last weight file.

        eg: filename = "weights/weights-improvement-47-1.2219-bigger.hdf5"
      
      *  Then, run $python TextGenerationSlow2.py

---

## Credits

Full credits for initial project to: 

https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/

---


