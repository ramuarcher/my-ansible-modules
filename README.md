# my-ansible-modules

This project writing custome ansible modules


Method1:

--> Execute custome module on local machine

    git clone ansible from github
    
    ```git clone https://github.com/ansible/ansible.git```
   
    
    ```source ansible/hacking/env-setup```
     
    ```ansible/hacking/test-module -m my-playbook/library/can_reach.py -a 'host=192.168.122.50 port=22 timeout=1'```

Method2:

---> create playbook directory in which you are going to create playbooks and python modules
    
     create library directory
     
     keep all your modules in library directory

    ````ansible-plabook playbook.yml library/can_reach.py```` 
