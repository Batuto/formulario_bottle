%rebase ./mysite/views/base.tpl page_title="People List"
<div class="panel panel-default">
    <div class="panel-heading">People</div>
    <div class="panel-body">
        <ul class="group-list">
            %for row in rows:
                %if not str(row[1]):
                    %var = "[!]-NULL"
                %else:
                    %id = row[0]
                    %name = row[1]
                %end
                <li class="list-group-item">
                    <span>
                        <a href="/item{{row[0]}}">{{id}} - {{name}}</a>
                        <a role="button" class="btn btn-danger btn-xs pull-right" href="/delete{{id}}">Delete</a> 
                    </span>
                </li>
            %end
        </ul>
    </div>
    <div class="panel-footer">
        <a role="button" class="btn btn-default" href="/new">Add New Register</a> 
    </div>
</div>
