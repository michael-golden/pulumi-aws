// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ElasticLoadBalancingV2
{
    [Obsolete(@"aws.elasticloadbalancingv2.getListener has been deprecated in favor of aws.lb.getListener")]
    public static class GetListener
    {
        /// <summary>
        /// &gt; **Note:** `aws.alb.Listener` is known as `aws.lb.Listener`. The functionality is identical.
        /// 
        /// Provides information about a Load Balancer Listener.
        /// 
        /// This data source can prove useful when a module accepts an LB Listener as an
        /// input variable and needs to know the LB it is attached to, or other
        /// information specific to the listener in question.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var config = new Config();
        ///         var listenerArn = config.Require("listenerArn");
        ///         var listener = Output.Create(Aws.LB.GetListener.InvokeAsync(new Aws.LB.GetListenerArgs
        ///         {
        ///             Arn = listenerArn,
        ///         }));
        ///         var selected = Output.Create(Aws.LB.GetLoadBalancer.InvokeAsync(new Aws.LB.GetLoadBalancerArgs
        ///         {
        ///             Name = "default-public",
        ///         }));
        ///         var selected443 = selected.Apply(selected =&gt; Output.Create(Aws.LB.GetListener.InvokeAsync(new Aws.LB.GetListenerArgs
        ///         {
        ///             LoadBalancerArn = selected.Arn,
        ///             Port = 443,
        ///         })));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetListenerResult> InvokeAsync(GetListenerArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetListenerResult>("aws:elasticloadbalancingv2/getListener:getListener", args ?? new GetListenerArgs(), options.WithVersion());
    }


    public sealed class GetListenerArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The arn of the listener. Required if `load_balancer_arn` and `port` is not set.
        /// </summary>
        [Input("arn")]
        public string? Arn { get; set; }

        /// <summary>
        /// The arn of the load balancer. Required if `arn` is not set.
        /// </summary>
        [Input("loadBalancerArn")]
        public string? LoadBalancerArn { get; set; }

        /// <summary>
        /// The port of the listener. Required if `arn` is not set.
        /// </summary>
        [Input("port")]
        public int? Port { get; set; }

        public GetListenerArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetListenerResult
    {
        public readonly string Arn;
        public readonly string CertificateArn;
        public readonly ImmutableArray<Outputs.GetListenerDefaultActionResult> DefaultActions;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string LoadBalancerArn;
        public readonly int Port;
        public readonly string Protocol;
        public readonly string SslPolicy;

        [OutputConstructor]
        private GetListenerResult(
            string arn,

            string certificateArn,

            ImmutableArray<Outputs.GetListenerDefaultActionResult> defaultActions,

            string id,

            string loadBalancerArn,

            int port,

            string protocol,

            string sslPolicy)
        {
            Arn = arn;
            CertificateArn = certificateArn;
            DefaultActions = defaultActions;
            Id = id;
            LoadBalancerArn = loadBalancerArn;
            Port = port;
            Protocol = protocol;
            SslPolicy = sslPolicy;
        }
    }
}
