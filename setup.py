from setuptools import setup
from setuptools import find_packages

setup(name='rgcn',
      version='0.0.1',
      description='Graph Convolutional Networks for (directed) relational graphs',
      download_url='...',
      license='MIT',
      install_requires=['numpy==1.12',
                        'theano==0.9.0',
                        'keras==1.2.1',
                        'rdflib',
                        'scipy==0.19.1',
                        'pandas==0.20.1',
                        'wget'
                        ],
      extras_require={
          'model_saving': ['h5py'],
      },
      package_data={'rgcn': ['README.md', 'rgcn/data']},
      packages=find_packages())
