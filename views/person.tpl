%rebase ./mysite/views/base.tpl page_title="People List"
%"""
%"""
<div class="panel-group">
    <div class="panel panel-default">
        <div class="well">
            <h2>{{name}}
                <br/><small>{{last_name}}</small>
            </h2>
        </div>
        <div class="panel-body">
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
            <label class="control-label col-sm-2 weirdo" for="reg_date">Registered:</label>
            </div>
            <div class="panel-body reg_date">
                {{regdatetime}}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
            <label class="control-label col-sm-2 weirdo" for="age">Age:</label>
            </div>
            <div class="panel-body age" name="age">
                {{age}}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
            <label class="control-label col-sm-2 weirdo" for="bio">Bio:</label>
            </div>
            <div class="panel-body age" name="bio">
                <p>{{bio}}</p>
            </div>
        </div>
    </div>
    <div class="panel-footer panel-default">
        <button class="btn btn-disabled" onClick=window.history.back()>Return</button>
        <button class="btn btn-default" onclick="location.href='/edit{{pid}}'">Edit</button>
        <button class="btn btn-danger" onclick="location.href='/delete{{pid}}'">Delete</button>
    </div>
</div>