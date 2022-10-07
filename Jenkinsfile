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
				sh 'chmod 777 build.sh'
				
				sh './build.sh'
				
			}				
        	}
        stage('Deploy Stage')
		{
			agent any
			steps
			{
				echo 'This is Deploy part'
				sh 'chmod 777 run.sh'
				sh './run.sh'
			
		
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
			echo 'Sorry. Build failed :('
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
