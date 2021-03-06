# Text Generation using LSTM
**Version 1.0**

Generative model for text using LSTM recurrent neural networks in Python with Keras

--- 

## Installation and Execution

1. Install Python and Keras on your device

2. Download this repository

3. To use the complex (but slow) neural network:

      * run $python TextGenerationLTSM1.py
      
      * change the 'filename' variable (line 57) to the weight file containing the lowest lost; typically the last weight file.

        eg: filename = "weights/weights-improvement-47-1.2219-bigger.hdf5" (or "weights\we..." on Windows, also change line 48 in LTSM1)
      
      *  Then, run $python TextGenerationLTSM2.py
      
      
   
   To use the faster (but less accurate) version:  
   
      * run $python TextGenerationFast1.py
      
      * change the 'filename' variable (line 46) to the weight file containing the lowest lost; typically the last weight file.

        eg: filename = "weights/weights-improvement-47-1.2219-bigger.hdf5" (or "weights\we..." on Windows, also change line 46 in Fast1)
      
      *  Then, run $python TextGenerationFast2.py
      
4. If you want to change the source, change lines at the top of all the files: 

      filename = "YOURTEXTHERE.txt"

---

## Screenshots

With more LSTM nodes, 20 epoch:

* we see that words are more English-like, complete whole terms albeit repeated due to the way we feed the seed

![ltsm1](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/ltsm1.JPG)

![ltsm2](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/ltsm2.JPG)

![ltsm3](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/ltsm3.JPG)


With less LSTM nodes, 20 epoch:

![fast1](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/fast1.JPG)

![fast2](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/fast2.JPG)

![fast3](https://github.com/chriskok/TextGenerationLTSM/blob/master/screenshots/fast3.JPG)

---

## Credits

Full credits for initial project to: 

  https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/

All text files downloaded from CreepyPasta and Project Gutenberg:

  https://www.creepypasta.com/
  
  http://www.gutenberg.org/

---


