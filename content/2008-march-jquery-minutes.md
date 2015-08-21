Title: March 2008 meeting minutes
Author: Joe
Date: 2008-03-09 11:38
Category: meetings
Tags: meeting-minutes, meetings-2008, jquery


Jquery Selectors:

The jquery selectors are used to select parts of a HTML document in a number of interesting ways.The selectors can be used to select say elements based on ids,classes,number etc.For example to select a html element with id="foobar" we can use $("#foobar") where $ is the factory function.

Jquery Event handlers:

Jquery has loads of event handlers associated with each HTML element and gave an introduction in an abstract way.


eg:

    :::javascript
    $(ul li a).click(function(){
        alert(($this).val());
    });

This will actually select all anchor tags within a li which is in turn inside a ul element and alert the value of the anchor.

JQuery and Ajax:

Jquery has some awesome support for asynchronous request and reply this includes methods like $get,$post methods.The $getJson method can be used to fetch a JSON file and parse it to obtain data.

Example: In our project DNS - Admim we have tried to use jquerys $get method with mod_python to delete a record when the user selects the zone name and type of record from a drop down list we send an asynchronous $get
request to fetchrecords.py with zone name and type as parameter and it will return the list of records.

JQuery Pluggins:

Gave an introduction about the variety of pluggins available in jquery one of the few interesting pluggins like calendar,form validation etc.
