import sublime, sublime_plugin,sys,re

 #   {
 #     type: 'text',
 #     value: "<?xml version='1.0' encoding='UTF-8'?>"
 #	   id: 'giveId'
 #   },


class makeJsonCommand(sublime_plugin.TextCommand):
    def run (self,edit):
        try:

            sels = self.view.sel()
            input = ''
            #print self.view.settings()
            for sel in sels:
                printPage = ''
                input = self.view.substr(sel)
                value = input.replace('\n', '\\n').replace('\t', '\\t').replace('"',"'") #.replace('/Up','\\"') add as many custom replacements as needed
                makeType = "'text'"
                makeId = "''"
                local="['US']"
                lang="['en','es']"
                translations="[]"
                dynamic = 'false'
                printPage = "\n{\n\ttype:%s,\n\tvalue:\"%s\",\n\tid:%s,\n\tlocal:%s,\n\tlang:%s,\n\ttranslations:%s,\n\tdynamic:%s\n}," %(makeType,value,makeId,local,lang,translations,dynamic)


                self.view.replace(edit,sel, printPage)
        except Exception:
            print ('something went wrong')