spm_encode --model=en_logic.model < data\english-train.txt > data\english-train.encoded.txt
spm_encode --model=en_logic.model < data\logic-train.txt > data\logic-train.encoded.txt
spm_encode --model=en_logic.model < data\english-val.txt > data\english-val.encoded.txt
spm_encode --model=en_logic.model < data\logic-val.txt > data\logic-val.encoded.txt
spm_encode --model=en_logic.model < data\english-test.txt > data\english-test.encoded.txt
spm_encode --model=en_logic.model < data\logic-test.txt > data\logic-test.encoded.txt