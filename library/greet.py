def main():
    module = AnsibleModule(
         argument_spec = dict(
             message = dict(required=True, type="str"),
         ),
         supports_check_mode=True
    )

    # get module params
    message = module.params.get("message")

    try:
      module.exit_json(changed=True, msg=message)
    except:
      module.fail_json(msg="It's bad not to greet someone")

  from ansible.module_utils.basic import *
  if __name__ == "__main__":
main()

