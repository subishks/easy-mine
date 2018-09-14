from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm 
from django.contrib import messages
from django.conf import settings
from shutil import copyfile
import shutil
import os


def upload_file(request):
    """ function for file_upload form and
         to show the data inside the file
    """

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        target = request.POST.get('target')
        if form.is_valid():
                myfile = request.FILES['file']
                file_data = myfile.read().decode('utf-8')
                file_data = file_data.strip(' ')
                file_data = file_data.split('\n')
                addnew_list = []
                modified_list = []       
                full_list = []        
                for data in file_data:
                    if data:
                        data=data.strip()             
                        if data[0] == 'M':
                            data = data.strip(' M')
                            modified_list.insert( len(modified_list),data)
                            full_list.insert( len(full_list),data)
                        elif data[0]  == 'A':
                            data = data.strip(' A')
                            addnew_list.insert( len(addnew_list),data)
                            full_list.insert( len(full_list),data)
                count_modified_files = len(modified_list)
                count_new_files = len(addnew_list) 

                str_full_list=",".join(full_list)
                return render(request,
                              'easy_mine/preview.html', 
                              {'form':form, 
                               'file_data':full_list,
                               'addnew_list':addnew_list,
                               'modified_list':modified_list,
                               'count_modified_files':count_modified_files,
                               'count_new_files':count_new_files,
                               'target':target,
                               'str_full_list':str_full_list
                               }
                             )
    else:
        form = UploadFileForm()
    
    return render(request, 'easy_mine/release.html', 
                  {'form': form}
                 )


def movefile(request):
    """ function to copy the files to target directories mentioned
        in the uploaded file
    """
    SOURCE_PREFIX = '/projects/test/CorePlatform/'      
    #give the desired prefix for the uploading file
    TARGET_PREFIX = '/home/digitalmesh/Documents/'      
    #give the desired prefix for the target directory
    file_data = request.POST.get('file_data')
    file_data = file_data.split(',')
    target = request.POST.get('target')
    error_file = []
    print(error_file)
    for source in file_data:
        try:
            if source:
                source=source.strip()
            source_path = SOURCE_PREFIX + source
            target_path = target + source
            target_path = TARGET_PREFIX + target_path
            directory = os.path.dirname(target_path)
            if os.path.exists(directory):
                shutil.copy(source_path, target_path)
            else:
                os.makedirs(directory)
                shutil.copy(source_path, target_path)
        except Exception as e:
            error_file.insert( len(error_file),source)
            continue
            
    success_msg = 'Successfully Copied the files to directories'
    error_msg = 'Error in path of Files'
    if(len(error_file) == 0):
        return render(request, 
                      'easy_mine/success.html', 
                      { 'success_msg':success_msg }
                     )
    else:
        return render(
                      request, 'easy_mine/success.html', 
                      { 'error_msg':error_msg, 
                       'error_file':error_file
                      }
                     )

   