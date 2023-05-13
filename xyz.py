import csv


def replace_text_in_file(file_path, old_text, new_text,new_path):
    with open(file_path, 'r') as file:
        content = file.read()
       






    
    updated_content = content.replace(old_text, new_text)
   
    with open(new_path, 'w') as file:
        file.write(updated_content)

# Example usage:
csv_file_path = 'abc.csv'
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        

        system_id = row[1]
        name= None
   


        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[1] == system_id:
                    name = row[2]
                    break

        
        if name:
            file_path = 'code.txt'
            old_text = '{name}'
            new_path =  "C:/Users/DELL/Desktop/fan/certificate/"+system_id +"_certificate.html"
            url=new_path

            replace_text_in_file(file_path, old_text, name,new_path)
            system_id1=str(system_id)
            print('HTML file created successfully for '+system_id1+' at '+new_path)
    



        else:
            print(f'System ID {system_id} not found.')

