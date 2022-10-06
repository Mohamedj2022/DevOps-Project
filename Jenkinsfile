pipeline 
{
    agent none
    stages 
	{
        stage('Build Stage')
		{
           		agent any
            		steps 
			{
				echo 'This is Build part'
			
				sh 'python app.py'
				
            		}
            	
        	}
        stage('Test Stage')
		{
			agent any
			steps
			{
				echo 'This is Test part'
			
				sh 'python test.py'
			}
		}
	stage('Admin Approval') 
		{
            		steps 
			{
                		input "Does the staging environment look ok?"
            		}
     		}
	}
post 
	{
	success 
		{
			echo 'Build Successfull!!'
		}
	failure 
		{
			echo 'Sorry mate! build is Failed :('
		}
	unstable 
		{
			echo 'Run was marked as unstable'
		}
	changed 
		{
			echo 'Hey look at this, Pipeline state is changed.'
		}
	}
}
