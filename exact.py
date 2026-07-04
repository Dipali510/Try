from Bio.Blast import NCBIWWW
import ssl
context=ssl._create_default_https_context=ssl._create_default_https_context_unverified_context()
seq="AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
print("performing blast search...")
result_handle=NCBIWWW.qblast("blastn","nt",seq,format_type="XML",ssl_context=context)
with open("blast_result.xml","w") as out_handle:
    out_handle.write(result_handle.read())
print("blast search completed")