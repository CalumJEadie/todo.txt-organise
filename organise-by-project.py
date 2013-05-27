#!/usr/bin/python

import fileinput
import re

project_regex = re.compile("\+(\S*)")
context_regex = re.compile("@(\S*)")

def project(todo):
    r = project_regex.search(todo)
    if r is None:
        return None
    else:
        return r.groups()[0]

def projects(todos):
    return set(map(project, todos))

def project_cmp(p1, p2):
        if p1 is None:
            return 1
        else:
            return cmp(p1, p2)

def context(todo):
    r = context_regex.search(todo)
    if r is None:
        return None
    else:
        return r.groups()[0]

def context_cmp(c1, c2):
        if c1 is None:
            return 1
        else:
            return cmp(c1, c2)

def todo_cmp(t1, t2):
    cmp_by_context = context_cmp(context(t1), context(t2))
    if cmp_by_context != 0:
        return cmp_by_context
    else:
        return cmp(t1, t2)

def main():
    todos = []
    for todo in fileinput.input():
        if todo != "":
            todos.append(todo)

    sorted_todos = sorted(todos, todo_cmp)
   
    projects_ = sorted(projects(todos), cmp=project_cmp)

    for project_ in projects_:
        project_todos = filter(lambda todo: project(todo) == project_, sorted_todos)
        print "".join(project_todos)
        # print ""

if __name__ == "__main__":
    main()