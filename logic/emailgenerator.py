import csv
import regex as re
from emailformat import *


# =============================================================================
# special formats = {
#   pH Pharma: jane.doe@ph-pharma.com,
#   Astex : jane.doe@astx.com,
#   Affini-T Therapeutics: jdoe@affiniatx.com,
#   Janssen: jdoe@its.jnj.com
#}
#  
# =============================================================================



first = ['Second Genome', 'ORIC Pharma', 'Asher Bio', 'AIVITA Biomedical',
         'REV Med']

firsttx = ['Scorpion']

firstrx = ['Arcturus']

lasttx = ['Flamingo']

firstlast = ['Tessa Therapeutics']

firstdotlast = ['AstraZeneca', 'Novartis', 'Pfizer', 'AVROBIO',
                'Biogen', 'Ipsen', 'Sanofi', 'BMS', 'Kronos Bio', 'Autolus',
                'Merck', 'Alexion', 'Bayer', 'Berg Health', 'EMD Serono',
                'Metabomed', 'Biogen','BioNTech', 'Regeneron','Takeda', 
                'Bicycle Therapeutics', 'Xilio', 'Boehringer Ingelheim', 
                'CG Oncology', 'Cyteir', 'Servier', 'Oncorus', 'Alkermes',
                'Astellas', 'Boston Pharmaceuticals', 'Editas Medicine',
                'SQZ Biotech', 'BERG Health', 'Cellectis', 'Codiak Bio',
                'Klus Pharma', 'Constellation Pharma', 'Legend Bio', 'Revitope',
                'Iovance', 'Roche', 'Gilead', 'AbbVie', 'BeiGene',
                'Fate Therapeutics', 'T-Cure', 'Alector', 'TP Therapeutics',
                'Mereo BioPharma', 'Ambrx', 'Immune Onc', 'Instil Bio', 'OncoMyx',
                'Alpine Immune Sciences', 'ONK Therapeutics', 'BridgeBio', 'Akeso Bio',
                'Xynomic Pharma', 'Jazz Pharma', 'Juno Therapeutics', 'Turnstone Bio',
                'I-Mab Biopharma', 'Nuvation Bio', 'Senti Bio', 'Sana', 'Cipla',
                'Genocea']

firstdotlasttx = ['Rubius', 'CRISPR', 'Strand','Moderna', 'Morphic', 'Nimbus',
                  'QED', 'Spotlight', 'Verseau', 'Intellia']

firstdotlastinc = ['Apollomics']

firstinitiallast = ['Blueprint Medicines', 'Celgene', 'Finch Therapeutics', 
                    'Bluebird Bio', 'FORMA Therapeutics', 'Epizyme', 
                    'Kura Oncology', 'Omega Therapeutics', 'LogicBio', 
                    'Cullinan Oncology', 'Karyopharm', 'Repertoire',
                    'Aura Biosciences', 'Ikena Oncology', 'Syros', 'OncXerna',
                    'Mersana', 'Poseida', 'Pyxis Oncology', 'Wugen', 'Surface Oncology',
                    'Checkmate Pharma', 'Deciphera', 'Verastem', 'Gossamer Bio',
                    'IDEAYA Bio', 'Immuneering', 'Lyell', 'Exelixis', 'Nektar',
                    'Clovis Oncology', 'Puma Biotechnology', 'Calidi Bio', 'Caribou Bio',
                    'CytomX', 'Denovo Biopharma', 'BryoLogyx', 'Illumina', 'VelosBio',
                    'Calithera', 'Atreca', 'Erasca', 'Amunix', 'Synthekine', 
                    'Arch Oncology', 'Artiva Bio', 'Bolt Bio', 'ESSA Pharma',
                    'Novome Bio', 'Sorrento Therapeutics', 'Coherus', 'Sutro Bio',
                    'Rigel', 'Atara Bio', 'Arcus Bio', 'Adicet Bio', 'Kite Pharma',
                    'Effector', 'RayzeBio', 'Viracta', 'ChemoCentryx', 'Oncternal',
                    'Kezar Life Sciences', 'NGM Bio', 'OncoSec','Loxo Oncology',
                    'Rain Thera', 'Pulse Biosciences', 'Theravance', 'Aptose',
                    'Amphivena', 'Apexigen', 'Inovio', 'PACT Pharma', 'Scholar Rock',
                    'Abpro', 'Dicerna', 'Vor Biopharma']   

firstinitiallasttx =['Tango', 'Werewolf', 'Skyhawk', 'Ribon', 'Cygnal', 
                     'Monte Rosa', 'Kymera', 'Foghorn', 'Immunitas', 'Repare',
                     'Relay', 'BlueRock', 'KSQ', 'Beam', 'Dewpoin', 'Harpoon',
                     'Heron', 'Bright Peak', 'Nurix', 'Notch', 'Tempest', 
                     'Silverback', 'Maverick', 'Verve', 'Arrakis', 'Obsidian']

firstinitiallastph = ['Ionis']

firstinitiallastbio = ['CERo']

firstdashlast = ['Allogene', 'H3 Biomedicine']

firstunderscorelast = ['Eisai', 'Adagene', 'PharmaEssentia']


company_lists = [first, firsttx, firstrx, lasttx, firstlast, firstdotlast, firstdotlasttx, firstdotlastinc,
              firstinitiallast, firstinitiallasttx, firstinitiallastph, firstinitiallastbio,
              firstdashlast, firstunderscorelast]

formatters = [first_name, first_tx, first_rx, last_tx, first_last, first_dot_last, first_dot_last_tx, first_dot_last_inc,
             first_initial_last, first_initial_last_tx, first_initial_last_ph, first_initial_last_bio,
             first_dash_last, first_underscore_last]
    
def csv_dic (csv_file):
    result = []
    reader = csv.DictReader(open(csv_file, encoding='utf-8-sig'))
    for row in reader:
        result.append(row)
    return result

def get_pattern(dic, company_list):
    result = []
    for i in company_list:
        pattern = re.compile(i, re.IGNORECASE)
        for company in re.findall(pattern, dic['company']):
            result.append(company)
    return result
    

def get_mapping(company_lists):
    company_list = []
    formatter_list = []
    for i,cl in enumerate(company_lists):
        company_list.extend(cl)
        formatter_list.extend(len(cl) * [formatters[i]])
    return company_list,formatter_list

company_list,formatter_list = get_mapping(company_lists)

def get_email(dic, company_list):
    pattern = get_pattern(dic,company_list)
    for company in pattern:
        if company not in company_list:
            continue
        formatter_list[company_list.index(company)](dic, company)
  

                    
 
data = csv_dic('data.csv')

for i in data:
    get_email(i, company_list)

print (data)

with open('result.csv', 'w', newline = '') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = data[0].keys())
    writer.writeheader()
    writer.writerows(data)
























