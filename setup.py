import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='funny_package',
      version='0.4',
      description='The funniest joke in the world',
      url='http://github.com/pawarrchetan/funny_package',
      author='pawarrchetan',
      author_email='pawarrchetan@gmail.com',
      long_description='The funniest joke in the world',
      long_description_content_type="text/markdown",
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      install_requires=[
          'markdown',
          'nose',
          'six',
      ],
      include_package_data=True,
      python_requires='>=3.6',
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/funniest-joke'],
      entry_points = {
        'console_scripts': ['funniest-joke=funny_package.command_line:main']
        })