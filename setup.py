from distutils.core import setup

setup(name='py_creoson_client',
      version='0.0.1',
      description='Python client for creoson library',
      author='Vyacheslav Krachkov',
      author_email='vskrachkov@gmail.com',
      packages=['pycreo', ],
      install_requires=[
            'requests'
      ],
     )