//On featureRequestDeatils.html load using ajax() get reqeust we will retrieve Json data from retrieveFeatureRequestManager function present in featurerequestmanager.py 
//After getting Json data it prints Json data to html
$(document).ready(function(){
    $.ajax({
        url: '/retrieveFeatureRequest',
        type: 'get',
        dataType: 'json',
        success: function(data){
            console.log("json"+data.details);
            $('#RequestList').DataTable({
                data: data.details,
                columns:[
                    { 'data': 'title' },
                    { 'data': 'description'},
                    { 'data': 'client'},
                    { 'data': 'clientPriority'},
                    { 'data': 'targetDate'},
                    { 'data': 'productArea'}
                ]
            });
        }
    });
});