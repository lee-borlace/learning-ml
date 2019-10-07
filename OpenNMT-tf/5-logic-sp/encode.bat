spm_encode --model=en_logic.model < english-train.txt > english-train.encoded.txt
spm_encode --model=en_logic.model < logic-train.txt > logic-train.encoded.txt
spm_encode --model=en_logic.model < english-val.txt > english-val.encoded.txt
spm_encode --model=en_logic.model < logic-val.txt > logic-val.encoded.txt
spm_encode --model=en_logic.model < english-test.txt > english-test.encoded.txt
spm_encode --model=en_logic.model < logic-test.txt > logic-test.encoded.txt