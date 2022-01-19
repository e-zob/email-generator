def first_name(dic, company):
    dic['email'] = dic['first_name'].lower() + '@' +  company.lower().replace(" ","") + '.com'

def first_tx (dic, company):
    dic['email'] = dic['first_name'].lower() + '@' +  company.lower().replace(" ","") + 'tx.com'

def first_rx (dic, company):
    dic['email'] = dic['first_name'].lower() + '@' +  company.lower().replace(" ","") + 'rx.com'
    
def last_tx (dic, company):
    dic['email'] = dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'tx.com'
    
def first_last(dic, company):
    dic['email'] =dic['first_name'].lower() + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + '.com'   

def first_dot_last(dic, company):
    dic['email'] =dic['first_name'].lower() + '.' + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + '.com'   

def first_dot_last_tx(dic, company):
    dic['email'] = dic['first_name'].lower() + '.' + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'tx.com'

def first_dot_last_inc(dic, company):
    dic['email'] = dic['first_name'].lower() + '.' + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'inc.com'

def first_initial_last(dic, company):
    dic['email'] = dic['first_name'][0].lower() + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + '.com'

def first_initial_last_tx(dic, company):
    dic['email'] = dic['first_name'][0].lower() + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'tx.com'

def first_initial_last_ph(dic, company):
    dic['email'] = dic['first_name'][0].lower() + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'ph.com'

def first_initial_last_bio(dic, company):
    dic['email'] = dic['first_name'][0].lower() + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + '.bio'
    

def first_dash_last(dic, company):
    dic['email'] = dic['first_name'].lower() + '-' + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + 'tx.com'

def first_underscore_last(dic, company):
    dic['email'] = dic['first_name'].lower() + '_' + dic['last_name'].lower() + '@' +  company.lower().replace(" ","") + '.com'

