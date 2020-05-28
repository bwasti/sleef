pipeline {
    agent any

    stages {
        stage('Preamble') {
            parallel {
                stage('x86') {
            	     agent { label 'x86' }
            	     steps {
	    	     	 sh '''
                	 echo "gcc-8 on" `hostname`
		         export CC=gcc-8
			 rm -rf build
 			 mkdir build
			 cd build
			 cmake -GNinja -DCMAKE_INSTALL_PREFIX=../install -DSLEEF_SHOW_CONFIG=1 -DENFORCE_TESTER3=TRUE -DBUILD_QUAD=TRUE ..
			 ninja
			 export OMP_WAIT_POLICY=passive
		         export CTEST_OUTPUT_ON_FAILURE=TRUE
		         ctest -j `nproc`
		         make install
			 '''
            	     }
                }

                stage('aarch64') {
            	     agent { label 'aarch64' }
            	     steps {
	    	     	 sh '''
                	 echo "gcc-8 on" `hostname`
		         export CC=gcc-8
			 rm -rf build
 			 mkdir build
			 cd build
			 cmake -GNinja -DCMAKE_INSTALL_PREFIX=../install -DSLEEF_SHOW_CONFIG=1 -DENFORCE_TESTER3=TRUE -DBUILD_QUAD=TRUE ..
			 ninja
			 export OMP_WAIT_POLICY=passive
		         export CTEST_OUTPUT_ON_FAILURE=TRUE
		         ctest -j `nproc`
		         make install
			 '''
            	     }
                }
            }
        }
    }
}
