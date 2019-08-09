
FMT-JSON
=========================

Loading script
-------------------------

Python script code should be added to the EOF block so that it can be set to the variable $FMT_JSON.

.. code:: bash
  
   FMT_JSON=$(cat <<'EOF'
     <add-script-here>
   EOF
   )


Running script
-------------------------

The python interpreter is called passing the script in via the ``-c`` argument. 

All following arguments apply to the script.

.. code:: bash

   ls -la ../ | python -c "$FMT_JSON" -h "permissions,count,owner,group,size,day,month,time_year,name" -P

The output to be parsed e.g. ``ls -la /`` should be piped to the python interpreter.
