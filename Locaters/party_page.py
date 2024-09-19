class Party:
    party_form = "//a[contains(text(), 'Party Form')]"
    first_middle_name = "(//label[contains(text(), ' F & M Name ')]/..//input)[1]"
    last_corporation_name = "(//label[contains(text(), ' Last/Corporation Name ')]/..//input)[1]"
    id_code = "(//label[contains(text(), ' ID Code ')]/..//select)[1]"
    seller_add_button = "(//button[contains(text(), ' Add ')])[4]"
    first_middle_name_2 = "(//label[contains(text(), ' F & M Name ')]/..//input)[2]"
    last_corporation_name_2 = "(//label[contains(text(), ' Last/Corporation Name ')]/..//input)[2]"
    id_code_2 = "(//label[contains(text(), ' ID Code ')]/..//select)[2]"
    seller_mail_address = "//input[contains(@id, 'custom-input_sellerMailFullStreetAddress_1')]"
    seller_mail_unit = "//input[contains(@id, 'custom-input_sellerMailUnitNumber_2')]"
    seller_mail_city = "//input[contains(@id, 'custom-input_sellerMailCity_3')]"
    seller_mail_state_dropdown = "//select[contains(@id, 'select_sellerMailState_4')]"
    seller_mail_zip = "//input[contains(@id, 'custom-input_sellerMailZip_5')]"
    seller_mail_zip4 = "//input[contains(@id, 'custom-input_sellerMailZip4_6')]"
    buyer_first_name = "(//label[contains(text(), ' F & M  Name ')]/..//input)[1]"
    buyer_corp_name = "(//label[contains(text(), ' Last/Corporation Name ')]/..//input)[3]"
    buyer_id_code = "(//label[contains(text(), ' ID Code ')]/..//select)[3]"
    buyer_care_of_name = "//input[contains(@id, 'custom-input_buyerMailCareOfName_1')]"
    buyer_visiting_code = "//select[contains(@id, 'select_buyerVestingCode_2')]"
    buyer_mail_address = "//input[contains(@id, 'custom-input_buyerMailFullStreetAddress_1')]"
    buyer_mail_unit = "//input[contains(@id, 'custom-input_buyerMailUnitNumber_2')]"
    buyer_mail_city = "//input[contains(@id, 'custom-input_buyerMailCity_3')]"
    buyer_mail_state_dropdown = "//select[contains(@id, 'select_buyerMailState_4')]"
    buyer_mail_zip = "//input[contains(@id, 'custom-input_buyerMailZip_5')]"
    buyer_mail_zip4 = "//input[contains(@id, 'custom-input_buyerMailZip4_6')]"



