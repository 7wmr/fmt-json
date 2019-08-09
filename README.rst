
FMT-JSON
=========================

Loading
-------------------------

Python script code should be added to the EOF block so that it can be set to the variable $FMT_JSON.

.. code:: bash
  
  FMT_JSON=$(cat <<'EOF'
    <add-script-here>
  EOF
  )


Execution
-------------------------

The python interpreter is called passing the script in via the ``-c`` argument. 

All following arguments apply to the script.

.. code:: bash

  ls -la / | python -c "$FMT_JSON" -h "permissions,count,owner,group,size,day,month,time_year,name" -P

The output to be parsed e.g. ``ls -la /`` should be piped to the python interpreter.


Output
-------------------------

See below a sample of the JSON data returned to the standard output.

::data:: array of objects: successfully parsed rows.
::errors:: array of arrays: any rows that could not be parsed
::status:: check of the parsed output: 0: success, 1: errors

.. code:: json

  {
      "data": [
          {
              "permissions": "drwxr-xr-x@",
              "count": 64,
              "owner": "root",
              "group": "wheel",
              "size": 2048,
              "day": 12,
              "month": "Jul",
              "time_year": "09:08",
              "name": "sbin"
          },
          {
              "permissions": "drwxr-xr-x@",
              "count": 10,
              "owner": "root",
              "group": "wheel",
              "size": 320,
              "day": 25,
              "month": "Sep",
              "time_year": 2018,
              "name": "usr"
          }
      ],
      "errors": [

      ],
      "status": 0
  }
