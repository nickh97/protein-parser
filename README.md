# protein-parser
Parse and format protein sequences
Accepts a .fasta file containing protein sequences and displays slices of the sequences to allow 
for easy comparison between different proteins (e.g., isolated from different bacterial strains).

Run from terminal using 'python ./protein-parser', must supply a file path to the .fasta file with
the sequences you want to process, as well as the amino acids to focus on as integers (i.e., the 
number in the sequence where the amino acids of interest are). Optionally,you can also specify how 
much buffer to include on either side of the focus pair and a name for the output file.

Example output, using the default buffer of 5:

              362          370          378          388          548     
CP9_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M22_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M45_chiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M78_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M79_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M81_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M84_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M85_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M87_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M90_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M91_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M92_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M93_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M94_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M95_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M96_ChiA   VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV
M111_ChiA  VYQNAWWVGSE  GSEDCPRGTSV  TSVENSNNPWR  RLVRTATAAEM  NGENYISQSKV

Still in development, base functionality is there but expect strange behavior, especially when using 
a large buffer or a lot of sample pairs. 

TODO: export table as a latex file to allow for advanced formatting/easier copy/paste. 
      test with DNA sequences to see if it works (it should, but still untested)
      improve row name-selecting function to be more flexible
