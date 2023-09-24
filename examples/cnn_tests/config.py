train = \
{

    #
    'epoch_number': 150,
    'initial_learning_rate': 0.01,
    'momentum': 0.9,
    
    'batch_size': 250,
    'validation_split': 0.1,
    'feature_number': 4,
    
    'device': 'cuda:0',
    'gpu_number': 2,
    'workers': 20,
    
    'save_model': True,
    'model_path': './model/',
    'model_name': 'test_model',
    
}

simulation = \
{

    #
    'pixel_size': 0.074,
    'galaxy_stamp_size': 128,
    'psf_stamp_size': 48,
    
    'read_noise': 5.0,
    'sky_background': 31.8,
    'dark_noise': 2.6,
    'bias_level': 500,
    'gain': 1.1,
    
}
