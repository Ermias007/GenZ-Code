def genz_interpreter(filename):
    context = {} # will be used to store variables and their data

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    def converter(term):

        conversion = {
            "gimmeMore": "+",
            "takeSome": "-",
            "stackUp": "*",
            "splitIt": "/",
            "leftover": "%",
            "itsGoood": "==",
            "itsBaaad": "!=",
            "better": ">",
            "worse": "<",
            "moreOrTwinning": ">=",
            "worseOrTwinning": "<=",
            "vibeWith": "and",
            "either": "or"
        }

        for genz, py in conversion.items():
            term = term.replace(genz, py)

        return term
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == "":
            i = i + 1
            continue

        if line.startswith("say("):
            message = line[4:-1]
            try:
                result = eval(converter(message), {}, context)
                print(result)
            except:
                if message.startswith('"') and message.endswith('"'):
                    print(message[1:-1])
                else:
                    print(message)

        elif "=" in line and not line.startswith("yea") and not line.startswith("nah"):
            parts = line.split("=")
            variable = parts[0].strip()
            value = parts[1].strip()

            if value == "fr":
                value = True
            elif value == "cap":
                value = False
            elif value == "ghost":
                value == None

            try:
                context[variable] = eval(converter(value), {}, context)
            except:
                context[variable] = int(value) if value.isdigit() else value

        elif line.startswith("loopy"):
            sections = line.split()
            loopy_var = sections[1]
            start = int(sections[3])
            end = int(sections[5].rstrip(":"))

            loop_index = i + 1
            if loop_index < len(lines):
                loopy_body = lines[loop_index].strip()

                for loopy_val in range(start,end+1):
                    context[loopy_var] = loopy_val

                    if loopy_body.startswith("say("):
                        message = loopy_body[4:-1]
                        try:
                            print(eval(converter(message), {}, context))
                        except:
                            if message.startswith('"') and message.endswith('"'):
                                print(message[1:-1])
                            else:
                                print(message)

                    elif "=" in loopy_body:
                        var, val = loopy_body.split("=")
                        var = var.strip()
                        val = val.strip()
                        try:
                            context[var] = eval(converter(val), {}, context)
                        except:
                            context[var] = val

            i+=2
            continue


        elif line.startswith("yea"):
            condition = line[3:].strip()
            if condition.endswith(":"):
                condition = condition[:-1]

            try:
                condition_outcome = eval(converter(condition), {}, context)
            except:
                condition_outcome = False

            if condition_outcome:
                i = i+1
                line_next = lines[i].strip()
                if line_next.startswith("say("):
                    message = line_next[4:-1]
                    try:
                        print(eval(converter(message), {}, context))
                    except:
                        if message.startswith('"') and message.endswith('"'):
                            print(message[1:-1])
                        else:
                            print(message)
                
                elif "=" in line_next:
                    parts = line_next.split("=")
                    variable = parts[0].strip()
                    value = parts[1].strip()
                    try:
                        context[variable] = eval(converter(value), {}, context)
                    except:
                        context[variable] = value
                i = i+1
                continue
            else:
                i= i + 2
                continue

        elif line.startswith("nah"):
            i=i+1
            line_next = lines[i].strip()
            if line_next.startswith("say("):
                message = line_next[4:-1]
                try:
                    print(eval(converter(message), {}, context))
                except:
                    if message.startswith('"') and message.endswith('"'):
                        print(message[1:-1])
                    else:
                        print(message)
            elif "=" in line_next:
                parts = line_next.split("=")
                variable = parts[0].strip()
                value = parts[1].strip()
                try:
                    context[variable] = eval(converter(value), {}, context)
                except:
                    context[variable] = value
            
        i= i+1
if __name__ == "__main__":
    genz_interpreter("simpleSample2.genz")


