# B-chromosomer

A pipeline for a reference-based assembly and annotation of low coverage microdissection samples.

## Prerequisites

- PyExp
- trseeker
- samtools
- bedtools
- bowtie2
- bamtools

## Assembly stages

Microdissection reads usually contain only small fraction of target sequences and are heavy contaminated by other DNA due to amplification step. To solve this problem I've developed B-chromosomer pipeline that map reads, filter our repeats, make chains and add external annotation to them.

Input data for pipeline should be cleaned out from possible adapters and low quality reads.

Pipeline include following stages:
1. Mapping all reads to the reference genome with bowtie2 program in global sensitive mode.
2. Removing all duplicates and unmapped reads with MQ<2 (unmapped and repeated).
3. Computing reads coverage with bedtools.
4. Joining chains with give spacer size with bedtools.
5. Extraction chain fasta and gff files.
6. Adding external gene and repeat annotation or any other if available.
7. Adding linkage group information according to the linkage group map.
8. Extraction gene annotation information including GO, KEGG, SwissProt, TrEMBL, and InterPro annotation for following manual analysis.

