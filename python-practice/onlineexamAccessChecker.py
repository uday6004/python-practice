print("Access Denied: System check Fa
else:
print("Access Granted")
elif not system_check:
print("Access Denied: Registration in
elif not fee_paid or not identity_verifie
print("Access Denied: Verification Pe
if not registered:

registered = input()
system_check = input()
identity_verified = input()
fee_paid = input()
# Check whether the student can access th
if not registered:
    print("Access Denied: Verification Pending")
    