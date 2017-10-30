%rebase ./mysite/views/report_base.tpl page_title="People List"
<div class="panel panel-default">
    <center><h2>Automatic Report</h2></center>
    <div class="panel-heading">People</div>
    <div class="panel-body">
        <ul class="group-list">
            %for row in rows:
                %if not str(row[1]):
                    %var = "[!]-NULL"
                %else:
                    %id = row[0]
                    %name = row[1]
                    %lastname = row[2]
                    %bio = row[3]
                    %age = row[4]
                %end
                <li class="list-group-item">
                    <span>
                        <a href="/item{{row[0]}}">{{id}} - {{name}} {{lastname}} {{age}} <br/> {{bio}} <br/></a>
                    </span>
                </li>
            %end
        </ul>
    </div>
</div>
