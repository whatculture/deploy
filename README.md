# deploy

Simple deploy script for staging & prod env.

### deploy master

    deployer config.yml

### deploy a branch

    deployer config.yml staging-branch
    
### rollback

    deployer config.yml rollback [version]
