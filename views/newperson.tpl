%rebase ./mysite/views/base.tpl page_title="New person"
<div class="panel panel-default">
    <div class="panel-heading">Add new people to the People list</div>
        <div class="panel-body">
            <form class="form-horizontal" action="/new" method="POST">
                <ul class="group-list">
                    <li class="list-group-item">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="name">Name:</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" placeholder="Enter name" name="name" required pattern="(([a-z]|[A-Z])+[ ]?)+"/>
                            </div>
                        </div>
                    </li>
                    <li class="list-group-item">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="last_name">Lastname:</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" placeholder="Enter lastname" name="last_name" required pattern="(([a-z]|[A-Z])+[ ]?)+"/>
                            </div>
                        </div>
                    </li>
                    <li class="list-group-item">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="age">Age:</label>
                            <div class="col-sm-10">
                                <input type="number" class="form-control" name="age" size="2" placeholder="Enter age" required pattern='\d{3}'/>
                            </div>
                        </div>
                    </li>
                    <li class="list-group-item">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="bio">Bio:</label>
                            <div class="col-sm-10">
                                <textarea name="bio" class="form-control" rows="10" cols="30" placeholder="Enter a short description" required></textarea>
                            </div>
                        </div>
                    </li>
                </ul>
                <div class="panel-footer">
                    <div class="col-sm-offset-2 col-sm-10">
                        <input type="submit" name="save" value="Save" class="btn btn-sucsess"/>
                        <button type="button" class="btn btn-default" name="cancel" onclick="parent.location='/'">Cancel</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>