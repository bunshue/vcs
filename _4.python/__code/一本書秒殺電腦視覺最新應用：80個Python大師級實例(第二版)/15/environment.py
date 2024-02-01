import gym
from gym import envs
import numpy as np
from helper_functions import rgb2gray,action_list,sel_action,sel_action_index
from keras import backend as K 

seed_gym = 3
action_repeat_num = 8
patience_count = 200
epsilon_greedy = True
max_reward =  10
grass_penalty  = 0.8
max_num_steps = 200 
max_num_episodes = action_repeat_num*100
'''智能体交互环境'''
class environment:    
    def __init__(self, environment_name,img_dim,num_stack,num_actions,render,lr):
        self.environment_name = environment_name
        print(self.environment_name)
        self.env = gym.make(self.environment_name)
        envs.box2d.car_racing.WINDOW_H = 500
        envs.box2d.car_racing.WINDOW_W = 600
        self.episode = 0
        self.reward = []    
        self.step = 0
        self.stuck_at_local_minima = 0
        self.img_dim = img_dim
        self.num_stack = num_stack
        self.num_actions = num_actions
        self.render = render
        self.lr = lr
        if self.render == True:
            print("显示proeprly数据集")
        else:
            print("显示问题")
             
    # 执行任务的智能体    
    def run(self,agent):
        self.env.seed(seed_gym)              
        img = self.env.reset()
        img =  rgb2gray(img, True)
        s = np.zeros(self.img_dim)
        #收集状态
        for i in range(self.num_stack):
            s[:,:,i] = img            
        s_ = s 
        R = 0
        self.step = 0                        
        a_soft = a_old = np.zeros(self.num_actions)
        a = action_list[0]       
        while True: 
            if agent.agent_type == 'Learning' : 
                if self.render == True :
                    self.env.render("human")
 

            if self.step % action_repeat_num == 0:                
                if agent.rand == False:
                    a_old = a_soft                
                #智能体的输出指令
                a,a_soft = agent.act(s)                
                # 智能体的局部最小值
                if epsilon_greedy:
                    if agent.rand == False:
                        if a_soft.argmax() == a_old.argmax():
                            self.stuck_at_local_minima += 1
                            if self.stuck_at_local_minima >= patience_count:
                                print('陷入局部最小值，重置学习速率')
                                agent.steps = 0
                                K.set_value(agent.DQN.opt.lr,self.lr*10)
                                self.stuck_at_local_minima = 0
                        else:
                            self.stuck_at_local_minima = max(self.stuck_at_local_minima -2, 0)
                            K.set_value(agent.DQN.opt.lr,self.lr)
                #对环境执行操作     
                img_rgb, r,done,info = self.env.step(a)            
                if not done:
                    # 创建下一状态
                    img =  rgb2gray(img_rgb, True)
                    for i in range(self.num_stack-1):
                        s_[:,:,i] = s_[:,:,i+1]
                    s_[:,:,self.num_stack-1] = img            
                else:
                   s_ = None
                # 累积奖励跟踪
                R += r
                # 对奖励值进行归一化处理
                r = (r/max_reward) 
                if np.mean(img_rgb[:,:,1]) > 185.0:
                # 如果汽车在草地上，就要处罚
                    r -= grass_penalty   
                #保持智能体值的范围在[-1,1]之间
                r = np.clip(r, -1 ,1)
                #Agent有一个完整的状态、动作、奖励和下一个状态可供学习
                agent.observe( (s, a, r, s_) )
                agent.replay()            
                s = s_            
            else:
                img_rgb, r, done, info = self.env.step(a)
                if not done:
                    
                    img =  rgb2gray(img_rgb, True)
                    for i in range(self.num_stack-1):
                        s_[:,:,i] = s_[:,:,i+1]
                    s_[:,:,self.num_stack-1] = img
                else:
                   s_ = None
                R += r
                s = s_                
            if (self.step % (action_repeat_num * 5) == 0) and (agent.agent_type=='Learning'):
                print('step:', self.step, 'R: %.1f' % R, a, 'rand:', agent.rand)
            
            self.step += 1
            
            if done or (R <-5) or (self.step > max_num_steps) or np.mean(img_rgb[:,:,1]) > 185.1:
                self.episode += 1
                self.reward.append(R)
                print('Done:', done, 'R<-5:', (R<-5), 'Green >185.1:',np.mean(img_rgb[:,:,1]))
                break
        print("集 ",self.episode,"/", max_num_episodes,agent.agent_type) 
        print("平均集奖励:", R/self.step, "总奖励:", sum(self.reward))   
    
    def test(self,agent):
        self.env.seed(seed_gym)
        img= self.env.reset()
        img = rgb2gray(img, True)
        s = np.zeros(self.img_dim)
        for i in range(self.num_stack):
            s[:,:,i] = img
        R = 0
        self.step = 0
        done = False
        while True :
            self.env.render('human')                            
            if self.step % action_repeat_num == 0:
                if(agent.agent_type == 'Learning'):
                    act1 = agent.DQN.predict_single_state(s)
                    act = sel_action(np.argmax(act1))
                else:
                    act = agent.act(s)                    
                if self.step <= 8:
                    act = sel_action(3)                    
                img_rgb, r, done,info = self.env.step(act)
                img = rgb2gray(img_rgb, True)
                R += r        
                for i in range(self.num_stack-1):
                    s[:,:,i] = s[:,:,i+1]
                s[:,:,self.num_stack-1] = img            
            if(self.step % 10) == 0:
                print('Step:', self.step, 'action:',act, 'R: %.1f' % R)
                print(np.mean(img_rgb[:,:,0]), np.mean(img_rgb[:,:,1]), np.mean(img_rgb[:,:,2]))
            self.step += 1
            
            if done or (R< -5) or (agent.steps > max_num_steps) or np.mean(img_rgb[:,:,1]) > 185.1:
                R = 0
                self.step = 0
                print('Done:', done, 'R<-5:', (R<-5), 'Green> 185.1:',np.mean(img_rgb[:,:,1]))
                break
