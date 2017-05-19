"""sequences.py hold the handle sequences used for the defined layout
change sequences here and they will be used throughut the analysis
"""

#################### WFA system ##############################################################################
#H1  = 'CAGTTGATCATCAGCAGGTAATCTGG'#'GGAGCCATTAAGTCGTAGCT' #H770
#DBS = 'BDHVBDHVBDHVBDHVBDHV'
#H2 = 'GACAGTTCCAAGAGGTCATG' #H1691
#H3 = 'TAGGACCAGCGTCTCAGTAT' #H4328
#################### WFA system ##############################################################################

#################### WFA2 system ##############################################################################
WFA_H1  = 'CAGTTGATCATCAGCAGGTAATCTGG' #E
WFA_DBS = 'BDHVBDHVBDHVBDHVBDHV'
WFA_H2 = 'CTGTCTCTTATACACATCTCATGAGAACGTCGTTGACGATGGACAGTTCCAAGAGGTCATG' #H1691'+H5+TES
WFA_H3 = 'TAGGACCAGCGTCTCAGTAGAGATGTGTATAAGAGACAG' #H43283'G+TES
#################### WFA system ##############################################################################


#################### ChIB system #############################################################################
# COMMENTS
#   - Incorporate H1, H2, H3, H4 for new system.

import seqdata
ChIB_H1 = 'GCCTGCACACTACAGCGTCC'
ChIB_H2 = 'AATTACCAGGCCAGTCGGTC'
ChIB_H3 = 'GATATTGCACGGTTGAACGG'
#ChIB_H4_H5_H6 = seqdata.revcomp('ACGGTTCCTCAATGTCTGCCGTAACCTCGGCATTATCGCGGTATTGGACAGGACCT')
ChIB_H4 = 'ACGGTTCCTCAATGTCTGCC'
ChIB_H5 = 'GTAACCTCGGCATTATCGCG'
ChIB_H6 = 'GTATTGGACAGGACC' #Change to real H6, some of H5 included in handle and 3' T.  
ChIB_DBS = 'NNNNNNNNAATTACCAGGCCAGTCGGTCNNNNNNNNGATATTGCACGGTTGAACGGNNNNNNNN'
#ChIB_H6prim = seqdata.revcomp('GGTCCTGTCCAATAC')
ChIB_H7 = 'CGGTCTTGGCTTGTCCTT' # REAL SEQ 'CGGTCTTGGCTTGTCCTTGC' shortend by two due to NN bases called for frist two bases in reverse read //PH
#################### ChIB system #############################################################################

#################### HLA system ##############################################################################
import seqdata
HLA_H1  = 'ACCGAGTGGTGAGTCATAGT'
HLA_DBS = 'BDVHBDVHBDVHBDVHBDVH'
HLA_H2 = seqdata.revcomp('CTAGCTTCACGAGTTCATCG')
HLA_H3 = 'AGATGGCCGTTATGATAGCG'
#################### HLA system ##############################################################################

#################### Universal ##############################################################################
ILLI5 = 'AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT'
ILLI7 = 'AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG'
IND_HANDLE_1 = 'TTAGTCTCCGACGGCAGGCTTCAAT'
IND_HANDLE_2 = 'ACGCACCCACCGGGACTCAG'
#################### Universal ##############################################################################

def sequence_layout(layout='HLA'):

    if layout == 'HLA':
        H1 = HLA_H1
        H2 = HLA_H2
        H3 = HLA_H3
        DBS= HLA_DBS
    elif layout == 'WFA':
        H1 = WFA_H1
        H2 = WFA_H2
        H3 = WFA_H3
        DBS= WFA_DBS

    ########################################################################################
    # NEWSTUFF FROM FRICK
    # Comments
    #   - Can DBS be None without breaking stuff?
    #   - remember to Check if DBS can be removed.
    elif layout == 'ChIB':

        # Stuff which goes strait into HLA pipeline.
        H1 = ChIB_H1
        H2 = ChIB_H6    # NB ChIB H4 is imported as H2 due to structure of HLA pipeline.
        H3 = seqdata.revcomp(ChIB_H6)
        DBS = ChIB_DBS  # Remove if you find where this is used in the pipeline. Something imports it somewhere.

        # Custom object sequences for ChIB xyz barcode layout
        real_H1 = ChIB_H1   # Not necessary, same as H2, but less confusing for reading/writing ChIB scripts.
        real_H2 = ChIB_H2
        real_H3 = ChIB_H3
        real_H4 = ChIB_H4
        real_H5 = ChIB_H5
        real_H6 = ChIB_H6
        #real_H6prim = ChIB_H6prim
        #real_H7prim = ChIB_H7prim
        # Not necessary, same as H2, but less confusing for reading/writing ChIB scripts.

    #########################################################################################
    else:
        print 'Error: No layout specified.'
        return 1

    import seqdata
    
    output  = '#  \n'
    output += '#  The expected layout of inserts should be:\n'
    output += '#  \n'
    output += '#  H1-DBS-revcomp(H2)-someDNA-revcomp(H3)\n'
    output += '#  \n'
    output += '#  Using the currently defined sequences this should be:\n'
    output += '#  '+H1+'-'+DBS+'-'+seqdata.revcomp(H2)+'-someDNA-'+seqdata.revcomp(H3)+'\n'
    output += '#  '+'\n'
    output += '#  '+'With illumina handles this will be:'+'\n'
    output += '#  '+ILLI5+'-'+H1+'-'+DBS+'-'+seqdata.revcomp(H2)+'-someDNA-'+seqdata.revcomp(H3)+'-'+ILLI7+'\n'
    output += '#  '+'or if ligated the other direction might also occur:'+'\n'
    output += '#  '+ILLI5+'-'+H3+'-someDNA-'+H2+'-'+seqdata.revcomp(DBS)+'-'+seqdata.revcomp(H1)+'-'+ILLI7+'\n'
    
    return output

def main():
    print sequence_layout(layout='HLA')
    print sequence_layout(layout='WFA')
    print sequence_layout(layout='ChIB')


if __name__ == "__main__": main()
