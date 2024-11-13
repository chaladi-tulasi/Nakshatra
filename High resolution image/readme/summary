SUPER RESOLUTION IMAGES

High-resolution imaging is essential in astronomy to study celestial objects with more accuracy and precision. Observing fine details in astronomical images 
aids in understanding cosmic phenomena such as galaxy formation, star evolution, and planetary characteristics. This model's ability to reconstruct high-resolution
images from lower resolutions helps to reveal hidden details and structures, allowing researchers and astronomers to conduct more accurate analysis and obtain new 
insights into celestial objects.


The model architecture is based on Super-Resolution Generative Adversarial Networks (SRGAN), which combines a generator and a discriminator network to enhance the 
quality and resolution of images.
Generator:
The generator network is composed of several convolutional layers and residual blocks. It converts low-resolution images to high-resolution outputs by learning 
fine details and texture patterns.Residual blocks are used to improve the network’s capability to capture complex features, enhancing the generator's performance 
in reconstructing realistic, high-quality images.
Discriminator:
The discriminator distinguishes between real high-resolution images and the generated (upscaled) images. It uses convolutional layers followed by LeakyReLU activations
and down-sampling to predict whether an image is real or generated.A Binary Cross-Entropy (BCE) loss is used to train the discriminator to classify images, while Mean
Squared Error (MSE) loss ensures the quality of image reconstruction by minimizing the difference between the generated and real high-resolution images.
Training is conducted over multiple epochs, optimizing both the generator and discriminator with Adam optimizers to enhance model accuracy.


This project introduces a GAN-based approach specifically optimized for astronomical image reconstruction, an application that often suffers from unique noise 
patterns and lacks sufficient high-resolution data. Traditional image super-resolution techniques are not adapted to these unique characteristics whereas this 
model leverages domain-specific data to improve reconstruction accuracy for astronomical imaging. By enhancing the clarity of images under challenging conditions 
this model brings a solution to a critical problem in the field of astronomy.
