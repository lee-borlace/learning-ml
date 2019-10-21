## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## invoice status check multiple
* invoice_status
  - utter_please_wait
  - utter_invoice_paid
  - utter_another_invoice
* affirm
  - utter_invoice_number_please    

<!-- ## invoice status check one
* invoice_status
  - utter_please_wait
  - utter_invoice_paid
  - utter_another_invoice
* deny
  - utter_sign_off -->
