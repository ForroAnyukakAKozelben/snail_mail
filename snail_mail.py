

number_of_at_characters = email.count("@")
number_of_dot_characters = email.count(".")
position_of_at = email.find("@")
position_of_last_dot = email.rfind(".")

error_message_no_at = "Hiba: hiányzik az '@' jel."
error_message_too_many_at = "Hiba: túl sok '@' jel."
error_message_no_dot = "Hiba: hiányzik a pont ('.')."
error_message_no_username = "Hiba: nincs felhasználónév az '@' előtt."
error_message_no_domain = "Hiba: nincs domain az '@' után."
error_message_no_dot_in_domain = "Hiba: a domainben nincs pont."
error_message_no_server_name = "Hiba: a domain ponttal kezdődik."
error_message_no_tld = "Hiba: nincs TLD a domain végén."
error_message_short_tld = "Hiba: a TLD túl rövid."
error_message_invalid_username = "Hiba: a felhasználónév ponttal kezdődik."
ok_message = "Valid email address :)"

is_valid = True
while is_valid
    while True:
        if number_of_at_characters == 0:
            print(error_message_no_at)
            break
        elif number_of_at_characters > 1:
            print(error_message_too_many_at)
            break

        username = email[:position_of_at]
        domain = email[position_of_at + 1:]

        if number_of_dot_characters == 0:
            print(error_message_no_dot)
            break
        if username == "":
            print(error_message_no_username)
            break
        if domain == "":
            print(error_message_no_domain)
            break
        if domain.count(".") == 0:
            print(error_message_no_dot_in_domain)
            break
        if domain[0] == ".":
            print(error_message_no_server_name)
            break

        tld = domain[position_of_last_dot + 1:]
        if tld == "":
            print(error_message_no_tld)
            break
        if len(tld) <= 2:
            print(error_message_short_tld)
            break
        if username[0] == ".":
            print(error_message_invalid_username)
            break
        is_valid = False
        break

print(ok_message)

