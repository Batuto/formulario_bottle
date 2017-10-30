%rebase ./mysite/views/base.tpl page_title="Reports List"
<div class="panel panel-default">
    <div class="panel-heading">Reports</div>
    <div class="panel-body">
        <ul class="group-list">
            %for row in onlyfiles:
                    <li class="list-group-item"><a href="/static/reports/{{row}}">{{row}}</a></li>
            %end
        </ul>
    </div>
</div>
<form action="/reports" method="POST" class="panel-footer">
                    <input class="btn btn-default" type="submit" name="save" value="Generate Report">
                    <input class="btn btn-default" type="button" name="" value="Cancel" onClick=window.history.back()>
        </form>