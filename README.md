# Pretius Oracle Forms XML Randomizer

Pretius Low-code offers a service where XML versions of Oracle Forms FMB files can be processed by a tool which estimates the amount of effort for redevelopment of those FMB files into Oracle APEX.

Before sending us the files for estimation, it is highly recommended that you download the "Pretius Oracle Forms XML Randomizer" tool which randomizes or encrypts sensitive information (names, PL/SQL, and all other attributes) within the XML files, without changing the original structure. 

Doing so will allow Pretius Low-code to upload the data to a proprietary estimation tool without infringing any sensitive data or Intelectual Property.

# Features

The Randomizer app converts the files in the following manner:

* The Data-Block and Data-Block Items will be encrypted utilizing a one-way encryption called MD5. 
  * This encryption makes it impossible to get back to the source string.
* All other content in the XML will be randomized as numbers.
* PL/SQL end-of-line terminators are kept in order to calculcate the number of lines within program units & triggers

Finally, XML files prepared this way can be securely shared with Pretius Low-code.

# Release History
1.0.0 : February 2023 : Initial Verison


# Installation Quick-Start
The following chapter describes step-by-step instructions.

## Instructions

1. Convert your Oracle Forms FMBs to XML files using the latest version of Oracle Forms if possible. 
   * There are documents/information on how to use the frmf2xml tool to do this. 
   * The steps to do this can be found on this blog https://blogs.oracle.com/apex/post/forms-to-apex-converting-fmbs-to-xml
2. Ensure you have Python installed. In Windows, type **python** in the Command Line, and it will install it if not already installed.
3. Download the [latest release of Pretius Oracle Forms XML Randomizer](https://github.com/Pretius/pretius-oracle-forms-xml-randomizer/releases) from the repository
4. Unzip the **pretiusRandFormsXML.py** file from downloaded zip file and store it in the location you have your XML files from step 1.
5. Please review the **pretiusRandFormsXML.py** file before running (see picture below).

![Instructional Image](https://raw.githubusercontent.com/Pretius/pretius-oracle-forms-xml-randomizer/master/img/preview.png "Figure 1")

6. Once reviewed. In the Command Line, navigate to the location you have your XML files from step 1 (see the TERMINAL tab in the picture below, where the folder c:\1\POFXR is used)
7. Run the Python application using the command below (the  **--randomize-filenames** parameter is optional). If you look at the TERMINAL tab in the picture above, it shows the folder is c:\1\POFXR folder while running the command below.

``` 
python pretiusRandFormsXML.py *.xml --randomize-filenames
```

8. When complete, you should see that files have been written to a new **output** sub-folder (see picture above, top of the left-hand pane) with randomized filenames.
9. Please review all XML files that have just been created in the **output** sub-folder to ensure that they are sufficiently redacted and do not contain any business logic.
10. Once reviewed and happy, please zip up the files in the **output** sub-folder and send the zip file back to Pretius Low-code.

# Future developments
Please let us know



