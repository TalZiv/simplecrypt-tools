import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='SimpleCrypt-Tools',
     version='0.2',
     author="Tal Ziv",
     author_email="tal.ziv.w@gmail.com",
     description="A RSA utility class",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/TalZiv/simplecrypt-tools",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )