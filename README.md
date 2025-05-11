# AI-image-classifier

A deep convolutional neural network, **insightnet**, is trained on a dataset named **deepfake** consisting of **4012** images of two classes: 'ai-generated' and 'real' person images in order to discriminate between the two. These images were prepared by scraping images from Google search results using Selenium and split into train, test, and validation sets in a ratio of 75:15:10.

## Dataset

The dataset can be downloaded from [this link](https://drive.google.com/file/d/1QR-bdR0hj9124YeGm5L7zAoKvhqa8Y4X/view?usp=drive_link).

The web scraping code and the dataset creation scripts are provided in `scrapeweb.py` and `train_test_val_split.py` respectively.

## Model

The model **insightnet**'s training and testing code is provided in the notebook `insightnet.ipynb`.

The trained model can be downloaded from [this link](https://drive.google.com/file/d/18XCwg0auP2xqTAsSOE4IL01fbeCUdlDH/view?usp=sharing).

## Running the Application

Follow these steps to run the app locally within a particular directory:

1. **Clone the GitHub repository:**

   ```sh
   git clone https://github.com/Susmm/AI-image-classifier

2. **Navigate inside the AI-image-classifier directory and install all the necessary dependencies:**
  
   ```sh
   cd AI-image-classifier
   pip install -r requirements.txt

3. **Navigate to the application directory:**

   ```sh
   cd application
   
4. **Create a new folder named 'model' within it:**

   ```sh
   mkdir model

5. **Download the trained cnn model 'insightnet.h5' from [this link](https://drive.google.com/file/d/18XCwg0auP2xqTAsSOE4IL01fbeCUdlDH/view?usp=sharing) and move it inside the 'model' directory**

6. **Run the Streamlit app on localhost:**

    ```sh
    streamlit run app.py --server.enableXsrfProtection false

## Testing the application 

Upload an image of a person in jpg, jpeg or png format (size >= **224*224** px) and classifier will classify it as real or ai-generated.   

